public class Solution{
public int hIndex(int[] citations){
     Arrays.sort(citations);
     int max = 0;
     for(int i = citations.length-1;i>=0;i--){
         int j = citations.length-i;
         int toCompare = Math.min(j, citations[i]);
	 max = Math.max(max, toCompare);
     }	
     return max;
 }
}
