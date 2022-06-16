'''
Back to Back SWE: https://youtu.be/suj1ro8TIVY

4:51
提到一件關於用遞迴方式處理樹的時候，最重要的事情：

-- How do I process this single node and then defer all of the other work and let the 
recursion do its job.

第一：我們想要處理眼前這個節點是空的情況，我們會回傳'X'

if root is None:
        return 'X'

第二：當目前這個節點有值的時候，我們要把這個值加上左子樹的序列化結果，以及右子樹的序列化結果。

return str(root.data) + ',' + left_serialized + ',' + right_serialized

但是關於第二件事，我們尚未得到子樹的序列華結果之前，我們沒辦法做合併。
所以這時候我們應該要 ”DEFER THE WORK"
意思就是 -- 當我得到足夠的資訊時，我知道怎麼做我的工作。在那之前，我們就必須先序列化左子樹，以及右子樹。
當兩者都交到我手上的時候，我可以將這些資訊跟我本身的資訊合併，得到我本分應該貢獻的結果。

    left_serialized = serialize(root.left)
    right_serialized = serialize(root.right)
    return str(root.data) + ',' + left_serialized + ',' + right_serialized

'''


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def serialize(root):
    if root is None:
        return 'X'

    left_serialized = serialize(root.left)
    right_serialized = serialize(root.right)

    return str(root.data) + ',' + left_serialized + ',' + right_serialized


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

print(serialize(root))      # 1,2,4,X,X,X,3,X,X
