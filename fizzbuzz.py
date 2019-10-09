#reference from https://gist.github.com/jjhamshaw/901902/45c2b50a051886497abc73044c8d77f30759e118


def fizzbuzz num

	answer = []

	answer.push 'fizz' if num % 3 == 0
	answer.push 'buzz' if num % 5 == 0
	answer.push num if num % 3 != 0 and num % 5 != 0
	
	puts answer.join
end

