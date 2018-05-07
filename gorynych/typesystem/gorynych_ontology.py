from .ontology import Ontology
from .node import Node
from .edge import Edge
from .nodes import *
from .nodes.basic import *
from .edges import *
from .edges.basic import *
from .relation import Relation as R
from .enums.directions import DirectionsEnum

DIRECT = DirectionsEnum.direct
BIDIRECT = DirectionsEnum.bidirect

GORYNYCH_ONTOLOGY = Ontology(
    node_types=[
        # Basic types
        Node,
        agent.Agent,
        data.Data,
        event.Event,
        instant_event.InstantEvent,
        continious_event.ContiniousEvent,
        group.Group,
        infrastructure.Infrastructure,
        location.Location,
        organization.Organization,
        person.Person,
        document.Document,
        # Advanced types
        account.Account,
        email.Email,
        ip_address.IPAddress,
        nickname.Nickname
    ],
    edge_types=[
        Edge,
        aggregation.Aggregation,
        association.Association,
        composition.Composition,
        connection.Connection,
        containment.Containment,
        dependency.Dependency,
        includes.Includes,
        membership.Membership,
        ownership.Ownership,
        responsibility.Responsibility,
        usage.Usage
    ],
    relations=[
        R("Person", "Account", "Ownership", DIRECT),
        R("Person", "Email", "Ownership", DIRECT),
        R("Person", "Nickname", "Ownership", DIRECT),
        R("Account", "Nickname", "Usage", DIRECT),
        R("Email", "Nickname", "Usage", DIRECT)
    ]
)