#!/usr/bin/env ruby

string = ARGV[0].scan(/(?<=from:)(.*?)(?=\])|(?<=to:)(.*?)(?=\])|(?<=flags:)(.*?)(?=\])/).join(" ")
string.gsub!("    ", ",")
puts string