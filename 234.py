accounts = [
    ["John","johnsmith@mail.com","john_newyork@mail.com"],
    ["John","johnsmith@mail.com","john00@mail.com"],
    ["Mary","mary@mail.com"],
    ["John","johnnybravo@mail.com"]
    ]

def accountsMerge(accounts):
    accounts.sort(key=lambda x: x[0])  # sort by name first
    
    merged = []
    email_to_group = {}  # maps email -> index in merged

    for acc in accounts:
        name = acc[0]
        emails = set(acc[1:])
        
        groups_to_merge = set()
        
        # find which existing groups overlap
        for email in emails:
            if email in email_to_group:
                groups_to_merge.add(email_to_group[email])
        
        if not groups_to_merge:
            # no overlap → create new group
            merged.append([name, emails])
            idx = len(merged) - 1
            for email in emails:
                email_to_group[email] = idx
        else:
            # merge all groups into one
            idx = min(groups_to_merge)   # pick one group index
            merged[idx][1].update(emails)  # add new emails
            merged[idx][0] = name  # keep name
            
            # re-map emails to this group
            for email in merged[idx][1]:
                email_to_group[email] = idx
            
            # merge other groups into this one if multiple overlaps
            for g in sorted(groups_to_merge - {idx}, reverse=True):
                merged[idx][1].update(merged[g][1])
                for email in merged[g][1]:
                    email_to_group[email] = idx
                merged.pop(g)

    # format result: sort emails for each group
    result = []
    for name, email_set in merged:
        result.append([name] + sorted(email_set))

    return result
