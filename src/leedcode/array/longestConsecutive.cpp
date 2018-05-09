//
//  longestConsecutive.cpp
//  niuke
//
//  Created by Lili Wang on 11/8/16.
//  Copyright © 2016 Lili Wang. All rights reserved.
//


//#unordered_set用hash表来解决这个问题，先初始化一个hash表， 存储所有数组元素， 然后遍历这个数组， 对找到的数组元素， 去搜索其相连的上下两个元素是否在hash表中， 如果在， 删除相应元素并增加此次查找的数据长度， 如果不在， 从下一个元素出发查找。已经访问过的元素记录下来或者删除，因为访问过的长度已经知道了额

#include "longestConsecutive.hpp"
#include <unordered_set>
using namespace std;

int longestConsecutive::LongestConsecutive(vector<int> &num) {
    unordered_set<int> myset(num.begin(),num.end());
    int res=1;
    for(int current:num)
    {
        //vector 传递的num就是num的大小。我们从头循环到底
//        printf("current is %d\n",current);
        //以防万一 执行到map结束
        if(myset.find(current)==myset.end()) continue;
        
        //查找看是否含有current+1，or current-1 如果发现有连续的数据则将此连续数据删除  根据连续数据的最小与最大只差得到有多少连续值，当只有一个值时候其最大连续值为1
        myset.erase(current);
        int prev=current-1,post=current+1;
        
        while(myset.find(prev)!=myset.end())
        {
            printf("%d\n",prev--);
            myset.erase(prev--);
        }
        while(myset.find(post)!=myset.end())
        {
            printf("%d\n",post);
            myset.erase(post++);
        }
        printf("%d,%d,%d\n",res,post,prev);
        res=max(res,post-prev-1);
    }
    printf("res is %d\n",res);
    return res;
}