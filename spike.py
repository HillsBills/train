def get_rna(rna):
    return rna.replace('a', 'u').replace('t', 'a').replace('c', 'x').replace('g', 'c').replace('x', 'g')
    # a = u.replace('t', 'a')
    # x = a.replace('c', 'x')
    # c = x.replace('g', 'c')
    # g = c.replace('x', 'g')


print(get_rna('atcg'))
