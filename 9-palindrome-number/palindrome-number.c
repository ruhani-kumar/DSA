bool isPalindrome(int x) {
    double rev = 0;
    double num = x;
    if(x>0){
    while (x!=0)
    {
        double digit = x % 10;
        rev = rev * 10 + digit;
        x = x / 10;
    }
    }

    if (rev == num)
    {
        return true;
    }
    else 
    {
        return false;
    }
}