def ft_count(orig):
    res = {}
    str_set = set(orig)
    for ch in str_set:
        res.update({ch: orig.count(ch)})
    res = {k: v / len(orig) for k, v in sorted(res.items(), key=lambda x: x[1])}
    return res


def ft_huffman(p):
    assert (sum(p.values()) == 1.0)

    if len(p) == 2:
        return dict(zip(p.keys(), ['0', '1']))
    p_prime = p.copy()
    a1, a2 = ft_lowest_prob_pair(p)
    p1, p2 = p_prime.pop(a1), p_prime.pop(a2)
    p_prime[a1 + a2] = p1 + p2
    c = ft_huffman(p_prime)
    ca1a2 = c.pop(a1 + a2)
    c[a1], c[a2] = ca1a2 + '0', ca1a2 + '1'
    return c


def ft_lowest_prob_pair(p):
    assert (len(p) >= 2)
    sorted_p = sorted(p.items(), key=lambda x: x[1])
    return sorted_p[0][0], sorted_p[1][0]


s = input("Put your string for encryption: ")
ex3 = ft_count(s)
codes = ft_huffman(ex3)
print("Generated codes for symbols: ")
print(codes)
print("Resulting string: ")
print("".join([codes[a] for a in s]))
