for i in range(int(input())):
    s1, s2  = (input() for _ in range(2))

    s1_replace = dict()
    s2_replace = dict()

    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if c1 not in s1_replace:
                if c2 in s2_replace:
                    print("NO")
                    break
                s1_replace[c1] = c2
                s2_replace[c2] = c1
            elif c1 in s1_replace and s1_replace[c1] != c2:
                print("NO")
                break
    else:
        for c1, c2 in zip(s1, s2):
            if c1 in s1_replace:
                if c2 != s1_replace[c1]:
                    print("NO")
                    break
            if c2 in s2_replace:
                if c1 != s2_replace[c2]:
                    print("NO")
                    break
        else:
            print("YES")
