# Stack

- For something to be a stack, it'd have to be something that we can add to or remove from the same "in" similar to a can of tennis balls. This means that for the first ball that went in to come out, all the balls would need to come out first (i.e. LIFO)
- In software engineering, this concept is commonly seen in back paging of browser history (e.g. pages visits may start at IG then FB, YT, and X). To get back to the first visted page, IG, we'd need to back three times
- In a List, a stack is when we add through append and pop to and from the end, respectively
- In a Linked List, a stack should be head (Top) to tail (Bottom). This means that the None pointer of tail points to the bottom and that's because the None pointer that ends LL should not point to the top since pushing it would become O(N)
