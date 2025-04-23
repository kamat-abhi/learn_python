chai_type = {
    "masala": "masala chai",
    "ginger": "ginger chai",
    "mint": "mint chai"
}

print(chai_type)
chai_type["city"] = "New York"  # add
chai_type["mint"] = 30           # update
print(chai_type)
chai_type.pop("city") 
