print "Let's practice everything."
print 'You\'d need to know \'bout secapes with \\ that do \n newlines and \t tabs.'

poem="""
\tThe lovely world
with logic so firmly planted
cannot discerm \nthe needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print " ---------"
print poem
print "----------"


five=10-2+3-6
print "This should be five:%s"%five

def secret_formual(started):
	jelly_beans=started*8500
	jars=jelly_beans/1000
	crates=jars/100
	return jelly_beans,jars,crates
	
	
start_point=10000
beans,jars,crates=secret_formual(start_point)

print "With a starting point od: %d"%start_point
print "We'd have %d beans, %d jars, and %d creates."%(beans,jars,crates)

start_point=start_point/10

print "We can also do that this way:"
print "We'd have %d beans, %d jars,and %d crates,"%secret_formual(start_point)