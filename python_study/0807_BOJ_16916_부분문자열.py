#접두사와 접미사가 일치하는 최대 길이를 계산하는 배열 pi를 생성하는 함수
#이름이 pi인 이유는 prefix 에서 따오거나 
def create_pi(pattern_str):
    length = len(pattern_str)
    pi = [0] * length

    prefix_idx = 0
    
    for idx in range(1, length):
        while prefix_idx > 0 and pattern_str[idx] != pattern_str[prefix_idx]:
            prefix_idx = pi[prefix_idx - 1]

        if pattern_str[idx] == pattern_str[prefix_idx]:
            prefix_idx += 1
            pi[idx] = prefix_idx
        
        else:
            pi[idx] = 0

    return pi

def main():
    #원본 문자열
    text_str = input()
    t_length = len(text_str)
    #패턴 문자열
    pattern_str = input()
    p_length = len(pattern_str)

    pi = create_pi(pattern_str)
    j = 0

    for i in range(t_length):
        while j > 0 and text_str[i] != pattern_str[j]:
            j = pi[j-1]
        
        if text_str[i] == pattern_str[j]:
            j += 1

        if j == p_length:
            print(1)
            return
    print(0)

    pass

if __name__ == "__main__":
    main()