def solution(s):
    # Your code here
    braillecodes = [
        '100000',
        '110000',
        '100100',
        '100110',
        '100010',
        '110100',
        '110110',
        '110010',
        '010100',
        '010110',
        '101000',
        '111000',
        '101100',
        '101110',
        '101010',
        '111100',
        '111110',
        '111010',
        '011100',
        '011110',
        '101001',
        '111001',
        '010111',
        '101101',
        '101111',
        '101011']
    answer = ''
    for i in range(len(s)):
        if s[i]==' ':
            answer+='000000'
            continue
        if s[i].isupper():
            answer += '000001'
        answer+=braillecodes[ord(s[i].lower())-ord('a')]
        
    print(answer)


