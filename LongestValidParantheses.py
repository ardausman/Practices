
'''Tries to find the longes meaningful parantheses sequence and show it with explanation'''

def longestValidParentheses(s: str) -> int:
        valid_length = 0
        stak = [-1]

        for i in range(len(s)):
           if s[i] is  "(":
               stak.append(i)
           else:
               stak.pop()
               if len(stak) is not 0:
                   valid_length = max(valid_length, i - stak[len(stak) - 1])
               else:
                   stak.append(i)

        return valid_length

if __name__ == '__main__':
    input_str = input("Parantheses here: ")
    sol = longestValidParentheses(input_str)
    print(sol)
