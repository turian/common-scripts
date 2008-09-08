#!/usr/bin/perl -w

  use Statistics::PointEstimation;

  my @r=();
  for($i=1;$i<=32;$i++) #generate a uniformly distributed sample with mean=5   
  {

          $rand=rand(10);
          push @r,$rand;
  }

  my $stat = new Statistics::PointEstimation;
  $stat->set_significance(95); #set the significance(confidence) level to 95%
  $stat->add_data(@r);
  $stat->output_confidence_interval(); #output summary
  $stat->print_confidence_interval();  #output the data hash related to confidence interval estimation

  #the following is the same as $stat->output_confidence_interval();
  print "Summary  from the observed values of the sample:\n";
  print "\tsample size= ", $stat->count()," , degree of freedom=", $stat->df(), "\n";
  print "\tmean=", $stat->mean()," , variance=", $stat->variance(),"\n";
  print "\tstandard deviation=", $stat->standard_deviation()," , standard error=", $stat->standard_error(),"\n";
  print "\t the estimate of the mean is ", $stat->mean()," +/- ",$stat->delta(),"\n\t",
  " or (",$stat->lower_clm()," to ",$stat->upper_clm," ) with ",$stat->significance," % of confidence\n";
  print "\t t-statistic=T=",$stat->t_statistic()," , Prob >|T|=",$stat->t_prob(),"\n";
