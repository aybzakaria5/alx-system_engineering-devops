#!/usr/bin/env ruby

sender, number, flags = ARGV[0].match(/^.*\[from:(.*?)\].*\[to:(.*?)\].*\[flags:(.*?)\].*$/i).captures
puts "#{sender},#{number},#{flags}"
end
