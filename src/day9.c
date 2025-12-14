/*
 * Advent of Code 2025 - Day 9
 *
 * Author: Xiaohan
 * Date: 2025-12-09
 *
 * Description:
 *   Solution code for Day 9 of Advent of Code 2025.
 *   Test rectangle in rectilinear polygon.
 *
 * Usage:
 *   Compile: g++ day9.c -o day9
 *   Run: ./day9 input.txt
 */
 #include <boost/polygon/polygon.hpp>

 #include <vector>
 #include <iostream>
 #include <fstream>
 #include <algorithm>
 #include <cstdint>
 
 namespace gtl = boost::polygon;
 using namespace gtl::operators;
 typedef gtl::polygon_90_data<int> polygon_90;
 typedef gtl::polygon_90_set_data<int> polygon_90_set;
 typedef gtl::rectangle_data<int> rectangle;
 typedef std::vector<rectangle> rectangle_container;
 
 void calculate_area(std::vector<gtl::point_data<int> > &pts,
         std::int64_t &area1,
         std::int64_t &area2) {
     polygon_90 input_poly;
     gtl::set_points(input_poly, pts.begin(), pts.end());
     polygon_90_set poly_set;
     poly_set += input_poly;
     rectangle_container rects;
     poly_set.get_rectangles(rects);
 
     area1 = -1;
     area2 = -1;
     int len_pts = pts.size();
     for(int i = 0; i < len_pts-1; ++i) {
         for(int j = 0; j < len_pts; ++j) {
             int xmin = std::min(pts.at(i).x(), pts.at(j).x());
             int xmax = std::max(pts.at(i).x(), pts.at(j).x());
             int ymin = std::min(pts.at(i).y(), pts.at(j).y());
             int ymax = std::max(pts.at(i).y(), pts.at(j).y());
             polygon_90 rect_poly;
             std::vector<gtl::point_data<int>> pts_rect = {
                 gtl::point_data<int>(xmin, ymin),
                 gtl::point_data<int>(xmax, ymin),
                 gtl::point_data<int>(xmax, ymax),
                 gtl::point_data<int>(xmin, ymax)
             };
             gtl::set_points(rect_poly, pts_rect.begin(), pts_rect.end());
 
             std::int64_t intersect_area = 0;
             for(const auto& rect: rects) {
                 int xmin_rect = gtl::xl(rect);
                 int xmax_rect = gtl::xh(rect);
                 int ymin_rect = gtl::yl(rect);
                 int ymax_rect = gtl::yh(rect);
                 int intersect_w = std::max(0, std::min(xmax_rect, xmax) - std::max(xmin_rect, xmin));
                 int intersect_h = std::max(0, std::min(ymax_rect, ymax) - std::max(ymin_rect, ymin));
                 intersect_area += static_cast<std::int64_t>(intersect_w) * static_cast<int64_t>(intersect_h);
             }
             std::int64_t area = static_cast<std::int64_t>(xmax - xmin + 1) * static_cast<std::int64_t>(ymax - ymin + 1);
             area1 = std::max(area, area1);
             if(intersect_area == (xmax - xmin) * (ymax - ymin)) {
                 area2 = std::max(area, area2);
             }
         }
     }
 
     return;
 }
 
 int main(int argc, char* argv[]) {
     if(argc < 2) {
         std::cout << "[ERROR] NO input file!" << std::endl;
         return 1;
     }
 
     std::ifstream infile(argv[1]);
     if(!infile) {
         std::cerr << "Failed to open input.txt" << std::endl;
         return 1;
     }
     int x, y;
     char comma;
     std::vector<gtl::point_data<int> > pts;
     while(infile >> x >> comma >> y) {
         pts.emplace_back(x, y);
     }
 
     std::int64_t res1, res2;
     calculate_area(pts, res1, res2);
 
     std::cout << res1 << " " << res2 << std::endl;
 
     return 0;
 }