def restoreIpAddresses(self, s):

    res = []

    # valid length
    if len(s) < 4 or len(s) > 12:
        return res

    def explorer(depth, digits):

        if depth == 4:
            if sum(digits) == len(s):
                ip = ""
                l_idx = 0
                section = 0
                while section < 4:
                    new_part = s[l_idx : l_idx + digits[section]]
                    if len(new_part) > 1 and new_part[0] == "0":
                        ip = ""
                        break
                    if len(new_part) == 3 and int(new_part[0]) > 2:
                        ip = ""
                        break
                    ip += new_part
                    if section < 3:
                        ip += "."
                    l_idx += digits[section]
                    section += 1

                if ip != "":
                    res.append(ip)
            return

        for num_digits in range(1, 4):
            digits.append(num_digits)
            explorer(depth + 1, digits)
            digits.pop()

    explorer(0, [])
    return res


s = "172162541"
print(restoreIpAddresses(None, s))
