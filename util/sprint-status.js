var data = require("./data.json");
var users = [];
var user_idx = {};

for (var i=0; i<data.members.length; i++)
{
	var m = data.members[i];
	users.push({name:m.fullName, createCard:0, commentCard:0});
	user_idx[m.id] = i;
}

for (var i=0; i<data.actions.length; i++)
{
	var a = data.actions[i];
	var m = users[user_idx[a.idMemberCreator]];
	if(!m.hasOwnProperty(a.type))
	{
		m[a.type] = 0;
	}
	m[a.type]++;
}

var lists = [];
var list_idx = {};
for (var i=0; i<data.lists.length; i++)
{
	var l = data.lists[i];
	lists.push({name:l.name,complete:0,total:0});
	list_idx[l.id] = i;
}

re = /\[([0-9]*)\]/
for (var i=0; i<data.cards.length; i++)
{
	var c = data.cards[i];
	var l = lists[list_idx[c.idList]];
	if (l.name.indexOf("Tasks") == 0) // i.e. startwith
	{
		m = re.exec(c.name);
		if (m)
		{
			l.total += (+m[1]);
			for (var j=0; j<c.labels.length; j++)
			{
				if (c.labels[j].name == "Complete")
				{
					l.complete += (+m[1]);
					break;
				}
			}
		}
		else if (c.closed != true)
		{
			console.log("ERROR: Card missing estimate: ", c.name);
		}
	}
}

console.log("List,Completed,Units of work");
var total = 0;
for (var i=0; i<lists.length; i++)
{
	l = lists[i];
	if (l.total != 0)
	{
		total += l.total;
		console.log([l.name, l.complete, l.total].join(","));
	}
}

