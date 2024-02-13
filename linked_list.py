class LinkedList:
    class Item:
        value = None
        next = None

        def __init__(self, value):
            self.value = value

    head: Item = None

    def append_begin(self, value):
        item = LinkedList.Item(value)
        item.next = self.head
        self.head = item

    def append_end(self, value):
        current = self.head
        if current is None:
            self.head = LinkedList.Item(value)
            self.head.value = value
            return

        while current.next:
            current = current.next

        item = LinkedList.Item(value)
        current.next = item

    def append_by_index(self, value, index):
        if index == 0:
            self.append_begin(value)
            return

        current = self.head
        prev = None
        count = 0

        while current and count < index:
            prev = current
            current = current.next
            count += 1

        if current is None:
            raise IndexError("Индекс не диапозоне")

        item = LinkedList.Item(value)
        prev.next = item
        item.next = current

    def len(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def remove_first(self):
        if self.head is None:
            raise ValueError("Лист пустой")
        self.head = self.head.next

    def remove_last(self):
        if self.head is None:
            raise ValueError("Лист пусой")
        if self.head.next is None:
            self.head = None
            return

        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def remove_at(self, index):
        if self.head is None:
            raise ValueError("Лист постой")

        if index == 0:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        count = 0

        while current and count < index:
            prev = current
            current = current.next
            count += 1

        if current is None:
            raise IndexError("Индекс не диапозоне")

        prev.next = current.next

    def remove_first_value(self, value):
        if self.head is None:
            raise ValueError("Лист пустой")

        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head
        prev = None

        while current and current.value != value:
            prev = current
            current = current.next

        if current is None:
            raise ValueError("Значение не найдено")

        prev.next = current.next

    def remove_last_value(self, value):
        if self.head is None:
            raise ValueError("Лист пустой")

        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        last_match = None

        while current:
            if current.value == value:
                last_match = current
            prev = current
            current = current.next

        if last_match is None:
            raise ValueError("Значение не найдено")

        prev.next = last_match.next


my_list = LinkedList()
my_list.append_begin(4)
my_list.append_begin(5)
my_list.append_begin(6)  
my_list.remove_first()
my_list.remove_last()
my_list.remove_at(0)
my_list.remove_first_value(5)
my_list.remove_last_value(10)
