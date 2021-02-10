#include "Problem12.h"
#include <cmath>

using std::pow;
using std::log10;

string intToRoman(int num){
    string answer = "";
    for (int i = (int)log10(num); i >= 0; --i){
        int digit = ((num % (int)pow(10,i+1)) / (int)pow(10,i));
        switch (i){
            case 3:
                for (int j = 0; j < digit; ++j){
                    answer += "M";
                }
                break;   
            case 2:
                if (digit == 9){
                    answer += "CM";
                }
                else if (digit == 4){
                    answer += "CD";
                }
                else if (digit == 5){
                    answer += "D";
                }
                else if (digit > 5){
                    answer += "D";
                    for (int j = 5; j < digit; ++j){
                        answer += "C";
                    }
                }
                else{
                    for (int j = 0; j < digit; ++j){
                        answer += "C";
                    }
                }
                break;
            case 1:
                if (digit == 9){
                    answer += "XC";
                }
                else if (digit == 4){
                    answer += "XL";
                }
                else if (digit == 5){
                    answer += "L";
                }
                else if (digit > 5){
                    answer += "L";
                    for (int j = 5; j < digit; ++j){
                        answer += "X";
                    }
                }
                else{
                    for (int j = 0; j < digit; ++j){
                        answer += "X";
                    }
                }
                break;
            case 0:
                if (digit == 9){
                    answer += "IX";
                }
                else if (digit == 4){
                    answer += "IV";
                }
                else if (digit == 5){
                    answer += "V";
                }
                else if (digit > 5){
                    answer += "V";
                    for (int j = 5; j < digit; ++j){
                        answer += "I";
                    }
                }
                else{
                    for (int j = 0; j < digit; ++j){
                        answer += "I";
                    }
                }
                break;
        }
    }
    return answer;
}