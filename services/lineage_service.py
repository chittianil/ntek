from sqlalchemy.orm import Session
from project.models.lineage import Lineage
from project.repository.lineage_repo import get_all_edges
from project.utils.graphs import has_cycle


def add_lineage(db: Session, upstream_id: int, downstream_id: int):

    edges = get_all_edges(db)

    graph = {}

    for e in edges:
        graph.setdefault(e.upstream_dataset_id, []).append(
            e.downstream_dataset_id
        )

    if has_cycle(graph, downstream_id, upstream_id):
        raise Exception("Cycle detected in lineage graph")

    lineage = Lineage(
        upstream_dataset_id=upstream_id,
        downstream_dataset_id=downstream_id
    )

    db.add(lineage)
    db.commit()

    return lineage