select * from 
	(
		select cur, start, end , sum(manpower) over (ORDER by cur DESC) as a 
		from routine 
		where work_center = 'AS-01'
			and start >= -33 
			and end < -30 
			and cur <2610
	)
where a = 5
 
 

