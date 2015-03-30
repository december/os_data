#include <map>
#include <set>

 int last = -1, cur = -1;
 map<Page*, int> num, timing;
 set<int> unused;

 int findPage(Page *page)
 {
    cur++;
    if (num.find(page) != num.end())
        return num[page];
    int allo = unused.upper_bound(-1);
    num[page] = allo;
    timing[page] = cur;
    unused.erase(allo);
    if (cur - last > 3)
    {
        for (auto it = num.begin(); it != num.end(); ++it)
            if (timing[it->first] < last)
            {
                timing.erase(timing.find(it->first));
                num.erase(it);
            }
    }
    last = cur;
    return allo;
 }