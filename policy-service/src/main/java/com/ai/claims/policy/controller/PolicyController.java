package com.ai.claims.policy.controller;

import org.springframework.web.bind.annotation.*;
import java.util.*;

@RestController
@RequestMapping("/api/policy")
public class PolicyController {

    private static final List<Map<String, Object>> MOCK_POLICIES = List.of(
        Map.of(
            "policy_id", "POL1234",
            "insured_name", "John Doe",
            "coverage_type", "Comprehensive Marine",
            "valid_till", "2026-05-30",
            "insured_value_usd", 20000,
            "deductible_usd", 500
        ),
        Map.of(
            "policy_id", "POL5678",
            "insured_name", "Alice Waters",
            "coverage_type", "Third Party Marine",
            "valid_till", "2025-09-10",
            "insured_value_usd", 15000,
            "deductible_usd", 1000
        )
    );

    @GetMapping("/{policyId}")
    public Map<String, Object> getPolicyById(@PathVariable String policyId) {
        return MOCK_POLICIES.stream()
                .filter(p -> p.get("policy_id").equals(policyId))
                .findFirst()
                .orElse(Map.of("error", "Policy not found"));
    }
}
