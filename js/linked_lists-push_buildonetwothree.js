"use strict";

function Node(data) {
    this.data = data;
    this.next = null;
}

function push(head, data) {
    let my_node = new Node(data);
    my_node.next = head;
    return my_node;
}

function buildOneTwoThree() {
  let chained = push(null, 3);
  chained = push(chained, 2);
  chained = push(chained, 1);
  return chained;
}

console.log(buildOneTwoThree().data);