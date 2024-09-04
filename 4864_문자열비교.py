import sys
sys.stdin = open("input.txt", "r")

#KMP 알고리즘으로 풀기

def main():
    T = int(input())
    for test_case in range(1, T + 1):
        pattern = input()
        text = input()
        is_exist = 0

        p_length = len(pattern)
        t_length = len(text)

        pi = [0] * p_length

        prefix_idx = 0
        for idx in range(1, p_length):
            while prefix_idx > 0 and pattern[idx] != pattern[prefix_idx]:
                prefix_idx = pi[prefix_idx-1]
            
            if pattern[idx] == pattern[prefix_idx]:
                prefix_idx += 1
                pi[idx] = prefix_idx
            else:
                pi[idx] = 0
        
        j=0
        i=0
        while i < t_length:
            while j > 0 and text[i] != pattern[j]:
                j = pi[j-1]
            
            if text[i] == pattern[j]:
                if j == p_length - 1:
                    is_exist = 1
                    break
                else:
                    i += 1
                    j += 1
            else:
                i += 1


        print(f"#{test_case} {is_exist}")

if __name__ == "__main__":
    main()