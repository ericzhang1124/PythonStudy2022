import re
import time
str = "!!!!!! 哈哈哈哈 !!!!!!!!!!!!!!!!!!!!!!!!!!!aaaabbksdkfasdlfass fsdffdeeeeeee1233423jfalfja;sjfaskfn;ljkcjlaouq89345834753488488452hihfakjfkafjfeworuoqfjoaoweuroqjewfoafiewoiuroqweoriquoweuroquweroiqwkfdjhfasldfstr = aaaabbksdkfasdlfass fsdffdeeeeeee1233423jfalfja;sjfaskfn;ljkcjlaouq89345834753488488452hihfakjfkafjfeworuoqfjoaoweuroqjewfoafiewoiuroqweoriquoweuroquweroiqwkfdjhfasldf;alksjdlfjaslkdjflasdfkhjerghjdhdfhiuhgkhakhgjjjjjjjfhjshdjfkajshdfieahfkajdhfkajhwekhfakhdfkwaehfkjhkdhfkwaekhfjkahfkajhfkewhkjfh4eeeeeeeeee、、、、：：：：：：：：：：：：eeessssssssaddddsssfksjdflatttttttttalksjdlfjaslkdjflasdfkhjerghjdhdfhiuhgkhakhgjjjjjjjfhjshdjfkajshdfieahfkajdhfkajhwekhfakhdfkwaehfkjhkdhfkwaekhfjkahfkajhfkewhkjfh4eeeeeeeeee、、、、：：：：：：：：：：：：eeessssssssaddddsssfksjdflattttttttt"
# str = unicode(str)

def first_func():
    start_time = time.time()
    longgest = 1
    last_item = ""
    my_res = {}
    for i in str:
        current_item = i
        if current_item == last_item:
            longgest += 1
        else:
            longgest = 1
        last_item = current_item
        if i not in my_res:
            my_res[i] = longgest
        else:
            my_res[i] = longgest

    max_key = max(my_res, key=my_res.get)
    print(f"max key is {max_key}, max value is {my_res[max_key]}")
    end_time = time.time()
    print(f"first_func耗时：{end_time - start_time}")


def second_func():
    start_time = time.time()
    strll = list(str)
    strset = set(strll)

    dictionary = {}
    for ele in strset:
        current_max_str = max(re.findall(rf'({ele}+)', str))
        ele_max_long = len(current_max_str)
        dictionary[ele] = ele_max_long

    print(dictionary)
    max_key = max(dictionary, key=dictionary.get)

    print(f"max key is {max_key}, max value is {dictionary[max_key]}")
    end_time = time.time()
    print(f"耗时：{end_time - start_time}")


if __name__ == '__main__':
    # first_func()
    # second_func()
    my_dictionary = {
        "goodsA": 110,
        "goodsE": 90,
        "goodsC": 45.4,
        "goodsD": 12,
        "goodsB": 45.44
    }
    only_max_dictionary = max(my_dictionary)

    with_index_key_max_dictionary = max(my_dictionary, key=my_dictionary.get)

    print(only_max_dictionary)
    print(with_index_key_max_dictionary)
