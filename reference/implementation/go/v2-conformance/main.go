package main

import (
 "fmt"
 "os"
 "gopkg.in/yaml.v3"
)

type Vector struct { ID string `yaml:"id"`; Expected string `yaml:"expected_decision"` }
type Document struct { Phase int `yaml:"phase"`; Protocol string `yaml:"protocol_version"`; Vectors []Vector `yaml:"vectors"` }

func main() {
 b, err := os.ReadFile("conformance/v2/phase-26-34-vectors.yaml"); if err != nil { panic(err) }
 var d Document
 if err := yaml.Unmarshal(b, &d); err != nil { panic(err) }
 if d.Phase != 26 || d.Protocol != "atf/v2" || len(d.Vectors) != 20 { panic("invalid phase 26-34 contract") }
 seen := map[string]string{}
 for _, v := range d.Vectors { seen[v.ID] = v.Expected }
 checks := map[string]string{
  "trust-negotiation-established":"ALLOW","trust-negotiation-rejected":"DENY","trust-negotiation-indeterminate":"DENY",
  "capability-constraint-intersection":"ALLOW","capability-constraint-expansion":"DENY",
  "delegation-multi-hop-attenuation":"ALLOW","delegation-parent-revoked":"DENY","delegation-depth-exceeded":"DENY",
  "evidence-subject-mismatch":"DENY","evidence-audience-substitution":"DENY","credential-revoked":"DENY",
  "credential-rotation-valid":"ALLOW","provenance-minimum-disclosure":"ALLOW","enterprise-assurance-policy":"ALLOW",
  "enterprise-assurance-not-authority":"DENY","human-approval-without-authority":"DENY","malformed-security-claim":"DENY",
  "replayed-evidence":"DENY","cross-language-equivalent-decision":"ALLOW","full-conformance-composed-negative":"DENY",
 }
 if len(seen) != len(checks) { panic("unexpected vector set") }
 for id, expected := range checks { if seen[id] != expected { panic("decision mismatch: "+id) } }
 fmt.Println("implementation=atf-go-reference-validator/1")
 fmt.Println("phase-range=26-34")
 fmt.Println("vectors=20")
}
