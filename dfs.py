    ''' res = []
        def dfs(s, o, wordict):
            if not s:
                res.append(o[:-1])
            for w in wordict:
                l = len(w)
                if s.startswith(w):
                    dfs(s[l:], o + w + ' ', wordict)
        dfs(s, '', wordDict)
        return res '''