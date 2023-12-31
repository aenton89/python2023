import pytest
from singlelist import SingleList, Node

def test_join():
    list1 = SingleList()
    list2 = SingleList()

    # test, obie listy puste
    list1.join(list2)
    assert list1.is_empty()
    assert list2.is_empty()

    # test, jedna lista pusta, druga niepusta
    node1 = Node(1)
    node2 = Node(2)
    list2.insert_head(node1)
    list2.insert_tail(node2)
    list1.join(list2)
    assert list1.head == node1
    assert list1.tail == node2
    assert list1.length == 2
    assert list2.is_empty()

    # test jedna lista niepusta, druga pusta
    node3 = Node(3)
    node4 = Node(4)
    list1.insert_head(node3)
    list1.insert_tail(node4)
    list1.join(list2)
    assert list1.head == node3
    assert list1.tail == node4
    assert list1.length == 4
    assert list2.is_empty()

    # test, obie listy niepuste
    node5 = Node(5)
    node6 = Node(6)
    list2.insert_head(node5)
    list2.insert_tail(node6)
    list1.join(list2)
    assert list1.head == node3
    assert list1.tail == node6
    assert list1.length == 6
    assert list2.is_empty()

def test_clear():
    list1 = SingleList()
    node1 = Node(1)
    node2 = Node(2)
    list1.insert_head(node1)
    list1.insert_tail(node2)

    # test
    list1.clear()
    assert list1.is_empty()
    assert list1.length == 0

def test_remove_tail():
    list1 = SingleList()
    node1 = Node(1)
    node2 = Node(2)
    list1.insert_head(node1)
    list1.insert_tail(node2)

    # test
    removed_node = list1.remove_tail()
    assert removed_node == node2
    assert list1.head == node1
    assert list1.tail == node1
    assert list1.length == 1

    # test na pustej liscie
    empty_list = SingleList()
    with pytest.raises(ValueError):
        empty_list.remove_tail()