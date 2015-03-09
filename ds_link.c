#include "list.h"
struct test
{
    list_entry *entry;
    int data;
    test()
    {
        entry = (list_entry*)malloc(sizeof(list_entry));
        list_init(entry);
    }
};

void chain_add(test *t1, test *t2)
{
    list_add(t1->entry, t2->entry);
}

void chain_delete(test *t1)
{
    list_delete(t1->entry);
}

bool chain_empty(test *t1)
{
    return list_empty(t1->list)
}

test* chain_next(test *t1)
{
    return (test*)(list_next(t1->entry));
}

test* chain_prev(test *t1)
{
    return (test*)(list_prev(t1->prev));
}
