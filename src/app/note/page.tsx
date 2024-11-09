import { sql } from "@vercel/postgres";
import { Suspense } from "react";
import dynamic from "next/dynamic";

export default async function Pets() {
  // استعلام لجلب جميع الحيوانات الأليفة من الجدول
  const { rows } = await sql`
    SELECT * FROM fonts
  `;
  const PetsWithPagination = dynamic(() => import("./useVisit"), {
    loading: () => <p>Loading...</p>,
  });
  return (
    <section>
      <Suspense fallback={<p>Loading feed...</p>}>
        <PetsWithPagination rows={rows} />
      </Suspense>
    </section>
  );
}
