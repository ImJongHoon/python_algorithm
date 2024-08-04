import sys
sys.stdin = open("input.txt", "r")

BASEWORD = 5

max_num = 0

def teach_word(check_words, word_arr, max_teach, idx, teached_words):
    global max_num
    #더 이상 가르칠 수 없을 때
    if max_teach == 0 or idx >= len(check_words):
        cnt = 0
        for word in word_arr:
            #이미 배운 글자들
            is_know = 1
            for elem in word:
                if elem in teached_words:
                    continue
                else:
                    is_know = 0
                    break
            if is_know:
                #print(check_words, word_arr, max_teach, idx, teached_words)
                cnt += 1

        max_num = max(max_num, cnt)
        #비교 함수 작성
        return
    
    
    
    teached_words.add(check_words[idx])
    teach_word(check_words, word_arr, max_teach - 1, idx+1, teached_words)
    #print(teached_words)
    teached_words.remove(check_words[idx])
    teach_word(check_words, word_arr, max_teach, idx+1, teached_words)
    #print(teached_words)



def main():
    word_num, max_teach = map(int, input().split())
    #a, n, t, i, c 는 필수로 이해 필요.
    studied_str = set()
    studied_str = {"a", "n", "t", "i", "c"}
    words = [input() for _ in range(word_num)]
    max_teach = max_teach - BASEWORD

    if max_teach < 0:
        print(0)
        return
    
    check_words = set()
    word_sets = set()
    word_arr = []

    for word in words:
        for elem in word[4:-4]:
            if elem in studied_str:
                continue
            #한 단어에 들어있는 판단해야하는 글자
            word_sets.add(elem)
            check_words.add(elem)
        word_arr.append(list(word_sets))
        word_sets.clear()

            #print(elem, end=" ")
        #print()
    #print(check_words)
    teached_words = set()
    #print(type(teached_words))

    teach_word(list(check_words), word_arr, max_teach, 0, teached_words)

    #print(word_num, max_teach)
    print(max_num)


if __name__ == "__main__":
    main()