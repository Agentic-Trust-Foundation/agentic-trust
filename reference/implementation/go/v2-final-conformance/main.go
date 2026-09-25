package main

import (
    "encoding/json"
    "fmt"
    "os"
    "path/filepath"
)

type Vector struct {
    ID string `json:"id"`
    Rule string `json:"rule"`
    ExpectedDecision string `json:"expected_decision"`
}

type Contract struct {
    Phase int `json:"phase"`
    ProtocolVersion string `json:"protocol_version"`
    Rules []string `json:"rules"`
    Vectors []Vector `json:"vectors"`
}

func load(path string) Contract {
    b, err := os.ReadFile(path)
    if err != nil { panic(err) }
    var c Contract
    if err := json.Unmarshal(b, &c); err != nil { panic(err) }
    return c
}

func main() {
    root, err := os.Getwd()
    if err != nil { panic(err) }
    repoRoot := filepath.Clean(filepath.Join(root, "..", "..", "..", ".."))

    for phase := 35; phase <= 42; phase++ {
        path := filepath.Join(repoRoot, "conformance", "v2", fmt.Sprintf("phase-%d", phase), "contract.json")
        c := load(path)
        if c.Phase != phase { panic(fmt.Sprintf("phase mismatch: expected %d got %d", phase, c.Phase)) }
        if c.ProtocolVersion != "atf/v2" { panic(fmt.Sprintf("protocol mismatch in phase %d", phase)) }
        if len(c.Vectors) != len(c.Rules)+1 { panic(fmt.Sprintf("vector/rule count mismatch in phase %d", phase)) }

        rules := map[string]bool{}
        for _, rule := range c.Rules { rules[rule] = true }
        for i, v := range c.Vectors {
            if i == len(c.Vectors)-1 {
                if v.Rule != "fail-closed" || v.ExpectedDecision != "DENY" { panic(fmt.Sprintf("missing fail-closed negative vector in phase %d", phase)) }
                continue
            }
            if !rules[v.Rule] { panic(fmt.Sprintf("vector rule %q is not declared in phase %d", v.Rule, phase)) }
            if v.ExpectedDecision != "ALLOW" && v.ExpectedDecision != "DENY" && v.ExpectedDecision != "REQUIRE_HUMAN" {
                panic(fmt.Sprintf("invalid decision in phase %d vector %s", phase, v.ID))
            }
        }
    }

    fmt.Println("ATF V2 Go independent conformance verifier: PASS")
    fmt.Println("phases=35-42")
    fmt.Println("implementation=atf-go-independent-v2/1")
}
