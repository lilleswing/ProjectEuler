function Node(data) {
    this.data = data;
    this.next = null;
}

function length(head) {
    if (head === null) {
        return 0;
    }
    return 1 + length(head.next);
}

function count(head, data) {
    let total = 0;
    while (head != null) {
        if (head.data === data) {
            total += 1;
        }
        head = head.next;
    }
    return total;
}