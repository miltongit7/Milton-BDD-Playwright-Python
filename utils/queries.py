GET_USERS_CREDS='''SELECT username, password
	FROM public.users
	where user_status='Valid' '''