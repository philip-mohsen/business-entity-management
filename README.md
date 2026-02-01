# Architecture Decisions
In this project, we have opted to embed `pydantic` directly within the Domain Layer as a conscious trade-off between architectural purity and development velocity.

While traditional Clean Architecture advocates for a dependency-free domain using POPOs (Plain Old Python Objects), utilizing Pydantic models as our primary Domain Objects eliminates the need for redundant boilerplate, complex mapping logic, and manual validation across layer boundaries. This 'Pragmatic Clean' approach ensures that our business rules remains highly declarative, type-safe, and self-validating, while significantly reducing the cognitive load and maintenance overhead associated with manual Data Transfer Object (DTO) translation.

The accepted trade-off is **Long-term Flexibility** vs. **Immediate Productivity**. We are betting that the benefits of Pydantic’s powerful validation and reduced boilerplate outweigh the unlikely need to swap validation frameworks in the future.
