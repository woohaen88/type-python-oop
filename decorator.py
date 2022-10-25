def copyright(func):
    def new_func():
        print("이게 계속 추가됨ㅋㅋㅋ")
        func()

    return new_func


@copyright
def smile():
    print("smile!!!!")


@copyright
def angry():
    print("angry!!!!!!!!!")


@copyright
def love():
    print("love!!!!!!!!!!!!!!!!!!!!!!!!!!")


if __name__ == "__main__":
    # smile()
    # angry()
    # love()
    # smile = copyright(smile)
    # angry = copyright(angry)
    # love = copyright(love)

    smile()
    angry()
    love()
