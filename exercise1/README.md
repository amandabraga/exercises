# Exercise 1

## Answer:

The code to check oddity fails for negative odd numbers because `i % 2` returns -1 for them, so the condition `i % 2 == 1` will return false .

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
