A,B,C= map(int, input().split())

MaiorAB = (A + B + abs(A-B))/2
MaiorAB = (C + MaiorAB + abs(MaiorAB -C))/2

print(f"{int(MaiorAB)} eh o maior")