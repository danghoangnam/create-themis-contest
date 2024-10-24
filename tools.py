def choose(array) -> int:
    for i in range(len(array)):
        print(f"{i}. {array[i]}")
    ans = int(input("Chọn: "))
    return ans

def yesOrNo(string) -> bool:
    ans = input(string + " (y/n): ").lower()
    if ans == "y":
        return True
    else:
        return False