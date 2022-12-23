function prioritizeNodes(tree, targetVal) {
  // helper function to rearrange the children array
  function prioritize(node, targetVal) {
    if (!node.children) return; // base case: node has no children

    if (node !== tree) {
      // rearrange the children array of non-root nodes
      let prioritized = [];
      let nonPrioritized = [];
      node.children.forEach(child => {
        if (child.val === targetVal || hasDescendant(child, targetVal)) {
          prioritized.push(child);
        } else {
          nonPrioritized.push(child);
        }
      });
      node.children = [...prioritized, ...nonPrioritized];
    } else {
      // rearrange the children array of the root node
      let prioritized = [];
      let nonPrioritized = [];
      node.children.forEach(child => {
        if (child.val === targetVal || hasDescendant(child, targetVal)) {
          prioritized.push(child);
        } else {
          nonPrioritized.push(child);
        }
      });
      node.children = [...prioritized, ...nonPrioritized];
    }
  }

  // helper function to check if a node has a descendant with the target value
  function hasDescendant(node, targetVal) {
    if (!node.children) return false; // base case: node has no children
    if (node.children.some(child => child.val === targetVal)) return true;
    return node.children.some(child => hasDescendant(child, targetVal));
  }

  // depth-first traversal
  function traverse(node) {
    prioritize(node, targetVal);
    if (!node.children) return; // base case: node has no children
    node.children.forEach(traverse);
  }

  traverse(tree);
  return tree;
}