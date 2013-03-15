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

console.log("USER ACTIVITY");
console.log("=============");
console.log("Name,Cards created,Comments");
for (var i=0; i<users.length; i++)
{
	var u = users[i];
	console.log([u.name, u.createCard, u.commentCard].join(","));
}
console.log("");

var lists = [];
var list_idx = {};
for (var i=0; i<data.lists.length; i++)
{
	var l = data.lists[i];
	lists.push({name:l.name,total:0});
	list_idx[l.id] = i;
}

re = /\[([0-9]*)\]/
for (var i=0; i<data.cards.length; i++)
{
	var c = data.cards[i];
	var l = lists[list_idx[c.idList]];
	if (l.name.indexOf("Product Backlog") == 0) // i.e. startwith
	{
		m = re.exec(c.name);
		if (m)
		{
			l.total += (+m[1]);
		}
		else if (c.closed != true)
		{
			console.log("ERROR: Card missing estimate: ", c.name);
		}
	}
}

console.log("PRODUCT BACKLOG");
console.log("===============");
console.log("List,Units of work");
var total = 0;
for (var i=0; i<lists.length; i++)
{
	l = lists[i];
	if (l.total != 0)
	{
		total += l.total;
		console.log([l.name, l.total].join(","));
	}
}
console.log("");
console.log("Total=",total);

