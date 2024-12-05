use std::env;
use std::fs;


fn part1(){
  let contents = fs::read_to_string("input.txt").expect("");
  let (lefts, rights): (Vec<&str>, Vec<&str>) = contents
    .lines()
    .map(|line| line.split_once(' ').expect("couldn't split"))
    .unzip()
  // println!("{:}", contents);
  
}


fn main(){
  part1();
}