package oa.gg;

/**
 *
 * 给定一个由‘—’‘|’组成的图形， 问其中能形成多少个正方形。 注意要自己定义以什么格式输入（不能是2d array）
 * 例如： ________________
 *       |       |______|
 *       |_______|      |
 *       |       |______|
 *       |_______|______|
 *
 * 大概这意思吧，比如这个图就返回4（3个小的1个大的）。但是因为当时没想到合理的输入方式……后来面试官说你自己定义一个
 * struct{
 *     char val;
 *     int start;
 *     int end;
 * }
 * 我写的过程中发现不是很好计算就改了下struct包含一个起始坐标，长度和val的。 但最后还是没想出来什么好的办法就写了个暴力还没写完……希望聪明的朋友们集思广益给楼主点启发
 */
public class NumberOfSquare {
}

