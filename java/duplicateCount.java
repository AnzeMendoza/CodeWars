package com.sucho;

import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        duplicateCount("ciudad");
    }

    public static int duplicateCount(String text) {
        HashMap<String, Integer> counter = new HashMap<String, Integer>();
        char [] textAChar = text.toLowerCase().toCharArray();
        for(char c : textAChar){
            String sc = String.valueOf(c);
            if(counter.containsKey(sc)){
                counter.put( sc,counter.get(sc)+1);
            } else {
                counter.put(String.valueOf(c),1);
            }
        }
        int cout = 0;
        for(HashMap.Entry<String, Integer> m : counter.entrySet()){
            if(m.getValue() > 1){
                cout++;
            }
        }
        return cout;
    }
}
