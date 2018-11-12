select order_runs.match_id,maximum_runs, player_name from 
(select distinct max_run.match_id, over_id,innings_no,player_name,  maximum_runs from (select match_id , max(total_runs) as maximum_runs from 
(select match_id,over_id,innings_no, sum(total_runs) as total_runs from(select match_id,over_id,innings_no,sum(runs_scored) 
as total_runs from batsman_scored group by match_id,over_id,innings_no union all select match_id,over_id,innings_no,sum(extra_runs) as
total_runs from extra_runs group by match_id,over_id,innings_no ) A group by match_id,over_id,innings_no) B group by match_id) 
max_run join over_wise_run on over_wise_run.match_id = max_run.match_id and over_wise_run.total_runs = max_run.maximum_runs order by 1,2) 
order_runs;

