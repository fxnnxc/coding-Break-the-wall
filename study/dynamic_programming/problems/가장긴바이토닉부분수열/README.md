# 가장 긴 바이토닉 부분 수열

## [문제](https://www.acmicpc.net/problem/11054) 
![image](https://user-images.githubusercontent.com/52944973/103066029-5a5bb700-45fb-11eb-8d3c-b6ed9c3ee0c8.png)

가장 긴 바이토닉 수열의 길이 찾기

## 예제

[1,50,2,3,4,2,5,4,3,10,2,1]

=>[1,2,3,4,5,4,3,2,1]이 가장 긴 수열이다.


## 문제 풀이 전략

가장 긴 증가하는 수열의 길이를 찾는 방법을 이용한다. 우선 가장 긴 증가하는 수열의 길이 구한 뒤 (DP1),  주어진 리스트를 뒤집은 다음 다시 가장 긴 증가하는 수열의 길이를 구한다(DP2).
그 다음 DP2를 뒤집어서 DP!과 각 인덱스를 더한 뒤 max-1 를 출력한다.

가자 긴 증가하는 수열의 길이는 다음과 같다.


![image](https://user-images.githubusercontent.com/52944973/103330147-9a131a80-4aa3-11eb-9029-c1e413ea939f.png)



점화식을 통해서 DP를 채울 것이다.



![image](https://user-images.githubusercontent.com/52944973/103330196-c9c22280-4aa3-11eb-979d-21fcedcd2920.png)
![image](https://user-images.githubusercontent.com/52944973/103330198-cc247c80-4aa3-11eb-9ae0-d68faf65c596.png)
![image](https://user-images.githubusercontent.com/52944973/103330199-cd55a980-4aa3-11eb-8ce1-b28e4142e40c.png)
![image](https://user-images.githubusercontent.com/52944973/103330203-cf1f6d00-4aa3-11eb-8b9f-3034ab140faf.png)
![image](https://user-images.githubusercontent.com/52944973/103330278-1b6aad00-4aa4-11eb-87df-795ea473cef2.png)
![image](https://user-images.githubusercontent.com/52944973/103330288-26254200-4aa4-11eb-9b2b-7bbd1f97f203.png)
![image](https://user-images.githubusercontent.com/52944973/103330299-33423100-4aa4-11eb-9b36-e7f0bdade304.png)




## Results

해당 예시로는 6


