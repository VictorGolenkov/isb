#include <iostream>
#include <random>
#include <bitset>
#include <string>

using namespace std;
    
/**
 * Generates random binary a sequence of length 128
 *
 * @return string of generated binary sequence
*/
string generate() {
    std::random_device rd;
    std::mt19937_64 gen(rd());
    
    uint64_t part1 = gen();
    uint64_t part2 = gen();
    
    std::bitset<64> bits1(part1);
    std::bitset<64> bits2(part2);

    return(bits2.to_string() + bits1.to_string());
}

/**
 * Main function that generates and prints a random binary sequence
 * 
 * @return int Exit status code (0 for success)
 */
int main() {
    std::cout << generate() << std::endl;
    
    return 0;
}