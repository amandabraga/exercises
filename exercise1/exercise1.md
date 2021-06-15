# Exercise 1

## Answer:

The code to check oddity fails for negative numbers, because when dividing negative numbers by 2 the module
will always be 0 or -1, so the condition `i % 2 == 1` will always return false for negative odd numbers.

To fix the code, the most simple solution is changing the condition: Instead of
checking if `i % 2` is equal to 1, we should check if it's different from 0.

```java
public class Oddity {
    public static boolean isOdd(int i) { 
        return i % 2 != 0;
    }
}
```

A less efficient solution in terms of time but that also works is getting the absolute value of `i % 2`, as shown below:

```java
public class Oddity {
    public static boolean isOdd(int i) { 
        return Math.abs(i % 2) == 1;
    }
}
```
