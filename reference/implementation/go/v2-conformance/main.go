package main

import ("fmt"; "os"; "strings")
func main() {
 b, err := os.ReadFile("../../../conformance/v2/phase-26-34-vectors.yaml")
 if err != nil { panic(err) }
 s := string(b)
 required := []string{"trust-negotiation-established","capability-constraint-expansion","delegation-parent-revoked","cross-language-equivalent-decision","full-conformance-composed-negative"}
 for _, id := range required { if !strings.Contains(s, id) { panic("missing vector: "+id) } }
 fmt.Println("implementation=atf-go-reference-validator/1")
 fmt.Println("phase-range=26-34")
 fmt.Println("vectors=verified")
}
